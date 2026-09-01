"""Simple keyword-based router for support messages.

route(message) inspects a support message and decides which department should
handle it, how urgent it is, and whether a human is needed.
"""

DEPARTMENT_KEYWORDS = {
    "billing": [
        "bill", "billing", "invoice", "payment", "charge", "charged",
        "refund", "subscription", "card", "price", "pricing",
    ],
    "orders": [
        "order", "delivery", "deliver", "shipping", "shipment", "ship",
        "track", "tracking", "package", "return", "cancel",
    ],
    "account": [
        "account", "login", "log in", "sign in", "password", "username",
        "profile", "register", "sign up", "access", "locked",
    ],
}

URGENT_KEYWORDS = ["down", "outage", "urgent", "asap", "legal"]


def route(message):
    """Route a support message to a department with a priority and human flag.

    Returns a dict: {"department": ..., "priority": ..., "needs_human": ...}.
    """
    text = (message or "").lower()

    priority = "urgent" if any(word in text for word in URGENT_KEYWORDS) else "normal"

    department = None
    if text.strip():
        for dept, keywords in DEPARTMENT_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                department = dept
                break

    needs_human = department is None
    if department is None:
        department = "general"

    return {
        "department": department,
        "priority": priority,
        "needs_human": needs_human,
    }


if __name__ == "__main__":
    tests = [
        "I was billed twice and need a refund on my subscription.",
        "My order hasn't arrived yet and I need it ASAP!",
        "",
    ]

    for msg in tests:
        print(repr(msg), "->", route(msg))
