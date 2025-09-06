from __future__ import annotations
import json
from flask import current_app, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import art_bp
from app.utils.tracing import trace_route
from .forms import ArtForm
from .services import _save_png_placeholder
from ..extensions import db
from ..model import MediaAsset, JournalEntry
from ..ai.tasks import generate_art_prompt


@art_bp.route("/art/new", methods=["GET", "POST"], endpoint="art_new")
@login_required
@trace_route("art.new")
def new_art():
    form = ArtForm()
    prompt_text = None
    if form.validate_on_submit():
        language = current_user.language_pref or "en"
        mood = (form.mood_text.data or "").strip()
        if form.use_last_journal.data:
            last = (
                JournalEntry.query.filter_by(user_id=current_user.id, is_deleted=False)
                .order_by(JournalEntry.created_at.desc())
                .first()
            )
            if last:
                mood = (last.ai_summary or mood or "")[:200]
        if not mood:
            mood = "calm, hopeful abstract sunrise with gentle curves"

        try:
            # AI → art prompt (string)
            prompt_text = generate_art_prompt(mood, language) or mood
        except Exception as e:
            current_app.logger.error("AI art prompt failed", exc_info=True)
            prompt_text = mood  # fallback


        try:
            # Image generation stub (safe offline)
            rel_path = _save_png_placeholder(prefix="art")
            asset = MediaAsset(
                user_id=current_user.id,
                kind="abstract_art",
                source="ai_generated",
                file_path=rel_path,
                caption=prompt_text[:255],
                meta_json=json.dumps({"prompt": prompt_text}),
            )
            db.session.add(asset)
            db.session.commit()
            flash("Art created 🖼️", "success")
            return redirect(url_for("art.art_detail", asset_id=asset.id))
        except Exception as db_err:
            db.session.rollback()
            current_app.logger.error("DB error while saving art", exc_info=True)
            flash("Something went wrong saving your art.", "danger")

    return render_template("art/new.html", form=form, prompt_text=prompt_text)

@art_bp.route("/art/gallery", methods=["GET"], endpoint="art_gallery")
@login_required
@trace_route("art.art_gallery")
def gallery():
    items = []  
    try:
        items = (
            MediaAsset.query.filter_by(user_id=current_user.id, kind="abstract_art")
            .order_by(MediaAsset.created_at.desc())
            .all()
        )
        return render_template("art/gallery.html", items=items)
    except Exception as e:
        current_app.logger.error("Failed to fetch gallery", exc_info=True)

    return render_template("art/gallery.html", items=items)

@art_bp.route("/art/<int:asset_id>", methods=["GET"], endpoint="art_detail")
@login_required
@trace_route("art.detail")
def detail(asset_id: int):
    item = MediaAsset.query.filter_by(id=asset_id, user_id=current_user.id).first_or_404()
    return render_template("art/detail.html", item=item)
