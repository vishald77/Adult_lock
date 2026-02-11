def highlight_text(text, signals):

    # 🛡️ Defensive guard
    if not isinstance(signals, dict):
        return text

    highlighted = text

    for category, words in signals.items():
        if isinstance(words, list):
            for w in words:
                highlighted = highlighted.replace(
                    w,
                    f"<mark style='background-color:#ffcccc'>{w}</mark>"
                )

    return highlighted