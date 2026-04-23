from app.core.database import SessionLocal
from app.models.interaction import Interaction

# -----------------------------
# Log Interaction
# -----------------------------
def log_interaction(data: dict):
    db = SessionLocal()
    try:
        interaction = Interaction(**data)
        db.add(interaction)
        db.commit()
        db.refresh(interaction)
        return {
            "id": interaction.id,
            "hcp_name": interaction.hcp_name,
            "topic": interaction.topic
        }
    finally:
        db.close()


# -----------------------------
# Edit Interaction
# -----------------------------
def edit_interaction(interaction_id: int, updates: dict):
    db = SessionLocal()
    try:
        record = db.query(Interaction).filter(Interaction.id == interaction_id).first()

        if not record:
            return {"error": "Interaction not found"}

        for key, value in updates.items():
            if hasattr(record, key):
                setattr(record, key, value)

        db.commit()
        db.refresh(record)

        return {"message": "Updated successfully", "id": record.id}
    finally:
        db.close()


# -----------------------------
# Fetch HCP History
# -----------------------------
def fetch_history(hcp_name: str):
    db = SessionLocal()
    try:
        records = db.query(Interaction).filter(Interaction.hcp_name == hcp_name).all()

        return [
            {
                "id": r.id,
                "topic": r.topic,
                "follow_up": r.follow_up,
                "summary": r.summary
            }
            for r in records
        ]
    finally:
        db.close()
