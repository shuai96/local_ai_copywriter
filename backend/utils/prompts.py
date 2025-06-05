from backend.utils.logging_config import setup_logging

setup_logging()

def build_prompt(form: dict) -> str:
    product_name = form.get("product_name", "")
    product_features = form.get("product_features", "")
    target_audience = form.get("target_audience", "") or "大众"
    use_scenarios = form.get("use_scenarios", "") or "日常"
    tone = form.get("tone", "自然")
    style = form.get("style", "小红书种草风，300字")
    platform = form.get("platform", "通用")
    output_format = form.get("output_format", "text")
    lang = form.get("lang", "zh")

    lang_intro_map = {
        "en": "You are a professional copywriter. Please generate a high-quality, engaging marketing copy in English based on the following information.",
        "jp": "あなたはプロのコピーライターです。以下の情報に基づき、日本語で高品質かつ魅力的なプロモーション文を作成してください。",
        "zh": "你是一名专业文案策划，请根据以下信息生成高质量、吸引人的中文营销文案。"
    }
    lang_map = {
        "en": "英文",
        "jp": "日文",
        "zh": "中文"
    }
    lang_intro = lang_intro_map.get(lang, lang_intro_map["zh"])
    lang_ = lang_map.get(lang, "中文")

    format_tip_map = {
        "markdown": "请使用 Markdown 格式输出。\n",
        "html": "请使用 HTML 段落标签输出。\n"
    }
    format_tip = format_tip_map.get(output_format, "")

    prompt = (
        f"{lang_intro}\n"
        f"{format_tip}"
        f"产品名称：{product_name}\n"
        f"产品卖点/核心优势：{product_features}\n"
        f"目标人群：{target_audience}\n"
        f"使用场景：{use_scenarios}\n"
        f"平台风格：{platform}\n"
        f"语气风格：{tone}\n"
        f"输出风格：{style}\n"
        f"输出语言：{lang_}\n"
        f"请结合上述要素,逻辑清晰、重点突出地撰写一段极具吸引力和说服力的营销文案，突出产品价值，激发用户兴趣和购买欲望。"
    )
    return prompt

