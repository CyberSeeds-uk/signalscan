def compute_priority(trust, commercial, urgency, ease_of_repair, confidence):
    """Compute a priority score based on weightings used in priority-matrix.csv.

    trust, commercial, urgency, ease_of_repair, confidence are integers 1–3.
    Higher scores indicate higher priority.  Ease of repair is inverted (lower is higher priority).
    """
    return (trust * 2) + (commercial * 2) + (urgency * 3) + (4 - ease_of_repair) + confidence


def test_compute_priority_order():
    # Privacy notice fix: high trust (3), medium commercial (2), high urgency (3), low repair effort (1), high confidence (3)
    privacy = compute_priority(3, 2, 3, 1, 3)
    # Date picker fix: low trust (1), high commercial (3), high urgency (3), medium repair (2), medium confidence (2)
    date_picker = compute_priority(1, 3, 3, 2, 2)
    # DMARC: medium trust (2), low commercial (1), medium urgency (2), medium repair (2), high confidence (3)
    dmarc = compute_priority(2, 1, 2, 2, 3)
    assert privacy > date_picker > dmarc