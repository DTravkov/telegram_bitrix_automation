from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

class LeadMessage:
    def __init__(self, lead_record):
        
        self.lead_record = lead_record
        self.contact_data = None  
        self.id = lead_record.get('ID')
    
    async def fetch_contact_data(self):

        from calls import fetch_lead_contact_by_id
        contact_id = self.lead_record.get("CONTACT_ID")
        
        self.contact_data = await fetch_lead_contact_by_id(contact_id)
        
        return self.contact_data
    
    def get_info_message(self):

        if not self.contact_data:
            print(f"Contact data not loaded for lead_id : {self.id}")
            return "Contact data not loaded"

        fields = [
            ("ID", self.id),
            ("Lead's Name", self.contact_data.get('NAME')),
            ("Lead's Phone", self.contact_data["PHONE"][0]["VALUE"]),
        ]
        
        lines = []
        for key, value in fields:
            if value:
                lines.append(f"{key}: {value}")
            else:
                lines.append(f"{key}: N/A")
        
        return '\n'.join(lines)
    
    def create_keyboard(self):
        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Called", 
                    callback_data=f"called_{self.id}"
                )
            ],
            [
                InlineKeyboardButton(
                    "💬 Wrote", 
                    callback_data=f"wrote_{self.id}"
                )
            ],
            [
                InlineKeyboardButton(
                    "⏳ Postpone 2h", 
                    callback_data=f"postponed_{self.id}"
                )
            ]
        ]
        
        return InlineKeyboardMarkup(keyboard)
    
    async def send_message(self, update: Update):
        await self.fetch_contact_data()

        keyboard = self.create_keyboard()

        await update.message.reply_text(text=self.get_info_message(),reply_markup=keyboard)
    
