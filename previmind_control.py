import os
from dotenv import load_dotenv
import google.generativeai as genai
from database import conectar_supabase

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing Gemini API Key in environment variables.")
genai.configure(api_key=GEMINI_API_KEY)

class PreviMindEngine:
    def __init__(self):
        self.supabase_client = conectar_supabase()
        self.flash_model = "gemini-2.5-flash"  
        self.pro_model = "gemini-2.5-pro"     

    def search_jurisprudence_ai(self, search_query: str, user_tier: str) -> dict:
        """
        Scans and analyzes judicial thesis trends using real Gemini inference.
        Restricted to Pro and Premium users.
        """
        if user_tier == "Basico":
            return {
                "status": "denied",
                "message": "Recurso restrito ao plano Pro ou Premium. Faça o upgrade para liberar o PreviMind IA!"
            }

        try:
            model = genai.GenerativeModel(self.flash_model)
            prompt = (
                f"Atue como um analista de jurisprudência sênior especializado em Direito Previdenciário brasileiro. "
                f"Analise e extraia as principais tendências, teses aplicáveis e precedentes (STJ/STF) para o seguinte termo: '{search_query}'. "
                f"Seja extremamente conciso e técnico na resposta."
            )
            
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "extracted_thesis": f"Análise de Tese: {search_query}",
                "applicable_precedent": "Precedentes mapeados via IA",
                "ai_summary": response.text.strip()
            }
        except Exception as e:
            return {"status": "error", "message": f"Gemini API Error: {e}"}

    def generate_document_by_folder(self, folder_name: str, document_type: str, context_data: dict, user_tier: str) -> dict:
        """
        Assembles professional legal drafts utilizing Gemini Pro's advanced intelligence.
        Exclusive to Premium tier members.
        """
        if user_tier != "Premium":
            return {
                "status": "denied",
                "message": "O Gerador Inteligente de Petições exige assinatura do plano Premium (Selo Coroa 👑)."
            }

        try:
            model = genai.GenerativeModel(self.pro_model)
            client_name = context_data.get('client_name', 'SEGURADO')
            
            prompt = (
                f"Atue como um advogado previdenciarista sênior. Escreva uma minuta de peça jurídica "
                f"do tipo '{document_type}' para o cliente '{client_name}'. O documento deve ser arquivado na pasta '{folder_name}'. "
                f"Utilize uma linguagem extremamente técnica, menções a artigos da lei vigentes e a estrutura formal do padrão forense brasileiro."
            )
            
            response = model.generate_content(prompt)
            
            return {
                "status": "success",
                "folder_destination": folder_name,
                "document_title": f"Minuta_IA_{document_type.replace(' ', '_')}.txt",
                "preview_content": response.text.strip()
            }
        except Exception as e:
            return {"status": "error", "message": f"Gemini API Error: {e}"}