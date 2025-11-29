from telegram import Update



class LeadMessage:
    def __init__(self, lead_record) -> None:
        self.lead_record = lead_record

        self.id = lead_record['ID']
        self.title = lead_record['TITLE']
        self.contact_id = lead_record['CONTACT_ID']

    def get_info_message(self):
        fields = [
        ("ID", self.id),
        ("Title", self.title),
        ("Contact ID", self.contact_id),
        ]
    
        lines = []
        for key, value in fields:
            if value is not None:
                lines.append(f"{key} : {value}")
            else:
                lines.append(f"{key} : N/A")
        
        return '\n'.join(lines)
    
    async def send_message(self, update: Update):
        await update.message.reply_text(self.get_info_message())
