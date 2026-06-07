def format_result(result: dict) -> str:
    lines = []

    if result["corrected"].strip() != result["original"].strip():
        lines.append(f"📝 *Original:*\n`{result['original']}`\n")
        lines.append(f"✅ *Corrected:*\n`{result['corrected']}`\n")
    else:
        lines.append(f"✅ *Looks good!*\n`{result['original']}`\n")

    if result["errors"]:
        lines.append(f"🔴 *Errors ({len(result['errors'])}):*")
        for i, err in enumerate(result["errors"], 1):
            lines.append(f"{i}. `{err['wrong']}` — {err['message']}")
            if err["suggestions"]:
                tips = ", ".join(f"`{r}`" for r in err["suggestions"])
                lines.append(f"   💡 Try: {tips}")
        lines.append("")
    else:
        lines.append("🟢 *No errors found!*\n")

    lines.append(f"⭐ *Score:* {result['score']}/10")

    return "\n".join(lines)