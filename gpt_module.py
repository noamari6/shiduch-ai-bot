def generate_profile(data):
    return f"בחור בן {data.get('age')}, מהעיר {data.get('city')}, מחפש קשר רציני."

def suggest_improvements(chat_history):
    # ניתוח שיחה לדוגמה
    if "לא מתאים לי" in chat_history:
        return "נראה שהשיחה לא מתקדמת. אולי כדאי לעדכן את הכרטיס ולציין מה אתה כן מחפש."
    elif "ספרי לי על עצמך" in chat_history and "לא יודעת" in chat_history:
        return "אפשר להוסיף בכרטיס תחומי עניין או תחביבים כדי להקל על שיחה ראשונית."
    return "השיחה מתנהלת טוב. אפשר להמשיך לפי התחושה."
