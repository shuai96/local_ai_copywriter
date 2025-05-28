def generate_prompt(product_name, product_features, style):
    return f"""
你是一位文案撰写助手，请为以下产品生成一段适合小红书的种草文案：

产品名称：{product_name}
产品特点：{product_features}
文案风格：{style}

要求：
- 使用第一人称
- 添加 emoji
- 自然真实
- 最后带上 3 个流行标签
"""
