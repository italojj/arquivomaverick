"""
Script para popular o banco de dados com os dados iniciais da Gangue da Maverick
Executa automaticamente quando o backend inicia se o banco estiver vazio
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Garante que não quebre se a variável não estiver carregada ainda (segurança extra)
mongo_url = os.environ.get('MONGO_URL')
db_name = os.environ.get('DB_NAME', 'maverick_db')

if not mongo_url:
    print("❌ ERRO: MONGO_URL não encontrada. Configure as variáveis de ambiente.")
    exit(1)

client = AsyncIOMotorClient(mongo_url)
db = client[db_name]


# Dados dos membros (ORIGINAIS)
MEMBERS_DATA = [
    {
        "id": "ramon-001",
        "name": "Ramon",
        "nickname": "Marrom Bombom",
        "classification": "Agente do Caos",
        "description": "Lenda viva por ter dormido na escola. Botafoguense sofredor e fã incondicional da DC. Sheipado e desempregado, mas sempre pronto para arrancar risadas.",
        "characteristics": [
            "Dormiu na escola (feito histórico)",
            "Botafoguense sofredor",
            "Fã da DC",
            "Sheipado",
            "Engraçado por natureza",
            "Desempregado, futuro aluno de CeT"
        ],
        "current_status": "Desempregado, futuro aluno de CeT",
        "role": "Principal fornecedor de piadas",
        "photo_url": None
    },
    {
        "id": "ph-002",
        "name": "PH",
        "nickname": "Pedroco",
        "classification": "Autoridade Técnica",
        "description": "Muito alto e apaixonado por carros. Trabalha no Carcará Baja e é fã de Fórmula 1 e Lewis Hamilton. Faz Engenharia Mecânica e é respeitado pela maioria.",
        "characteristics": [
            "Muito alto (estatística relevante)",
            "Gosta de carros",
            "Trabalha no Carcará Baja",
            "Fã de Fórmula 1 e Lewis Hamilton",
            "Faz Engenharia Mecânica",
            "Respeitado pela maioria"
        ],
        "current_status": "Trabalhando no Carcará Baja, cursando Engenharia",
        "role": "Autoridade técnica",
        "photo_url": None
    },
    {
        "id": "julliano-003",
        "name": "Julliano",
        "nickname": "Juju do PIX",
        "classification": "Prova Viva da Inclusão",
        "description": "Último a entrar no grupo, mas ninguém nota. Sheipado, solteiro recente e corinthiano. Trabalha na Gilmar Enterprises e tirou habilitação recentemente.",
        "characteristics": [
            "Sheipado",
            "Solteiro recente",
            "Corinthiano",
            "Trabalha na Gilmar Enterprises",
            "Tirou habilitação recentemente",
            "Último a entrar no grupo (ninguém nota)",
            "Humorista nível avançado"
        ],
        "current_status": "Trabalhando na Gilmar Enterprises, recém habilitado",
        "role": "Prova viva de que a Maverick aceita todos",
        "photo_url": None
    },
    {
        "id": "italo-004",
        "name": "Ítalo",
        "nickname": "Cinema",
        "classification": "Infraestrutura Digital",
        "description": "Faz TI e é tryhard extremo em jogos. Dono do servidor do Discord, mas tem o péssimo hábito de trocar amigos por namorada. Nerd, porém respeitado.",
        "characteristics": [
            "Faz TI",
            "Troca amigos por namorada (crime recorrente)",
            "Tryhard extremo em jogos",
            "Dono do servidor do Discord",
            "Nerd, porém respeitado"
        ],
        "current_status": "Cursando TI, mantendo a infraestrutura digital",
        "role": "Infraestrutura digital",
        "photo_url": None
    },
    {
        "id": "felipe-005",
        "name": "Felipe",
        "nickname": "Careca",
        "classification": "Orgulho Acadêmico",
        "description": "Virjão cabaço segundo o banco de dados, mas extremamente dedicado. Corinthiano que passou em Medicina. Gera momentos únicos com seu jeito estranho.",
        "characteristics": [
            "Virjão cabaço (segundo o banco de dados)",
            "Extremamente dedicado",
            "Corinthiano",
            "Passou em Medicina",
            "Gera momentos únicos com seu jeito estranho"
        ],
        "current_status": "Cursando Medicina",
        "role": "Orgulho acadêmico e entretenimento involuntário",
        "photo_url": None
    },
    {
        "id": "gabriel-006",
        "name": "Gabriel",
        "nickname": "Biel",
        "classification": "Disciplina Militar",
        "description": "O mais sério do grupo. Foi pro Exército sem ser chamado, gosta de Pokémon e está sempre na dele. Namora, faz CeT e é flamenguista.",
        "characteristics": [
            "Mais sério do grupo",
            "Foi pro Exército sem ser chamado",
            "Gosta de Pokémon",
            "Na dele",
            "Namora",
            "Faz CeT",
            "Flamenguista"
        ],
        "current_status": "Cursando CeT, namorando",
        "role": "Disciplina e silêncio estratégico",
        "photo_url": None
    },
    {
        "id": "davi-007",
        "name": "Davi",
        "nickname": "Blackie Chan",
        "classification": "Alívio Cômico",
        "description": "O mais zoado do grupo, desrespeitado em tom de brincadeira. Namora à distância, tem histórico de webnamoro e troca amizades por namoro. Fluminense e trabalha na Teleperformance.",
        "characteristics": [
            "Mais zoado do grupo",
            "Desrespeitado em tom de brincadeira",
            "Namora à distância",
            "Histórico de webnamoro",
            "Troca amizades por namoro",
            "Fluminense",
            "Trabalha na Teleperformance"
        ],
        "current_status": "Trabalhando na Teleperformance, namorando à distância",
        "role": "Alívio cômico involuntário",
        "photo_url": None
    },
    {
        "id": "jordan-008",
        "name": "Jordan",
        "nickname": "Faguinho",
        "classification": "Vida Noturna",
        "description": "Famoso por trocar amigos por mulher. Flamenguista que faz CeT, bebe como se não houvesse amanhã e é baladeiro. Trabalha no Camarões.",
        "characteristics": [
            "Troca amigos por mulher",
            "Flamenguista",
            "Faz CeT",
            "Bebe como se não houvesse amanhã",
            "Baladeiro",
            "Trabalha no Camarões"
        ],
        "current_status": "Trabalhando no Camarões, curtindo a vida noturna",
        "role": "Vida noturna da gangue",
        "photo_url": None
    }
]

# Citações (ORIGINAIS)
QUOTES_DATA = [
    {"id": "quote-001", "text": "Quem namora é ela, não é tu", "member_id": "jordan-008"},
    {"id": "quote-002", "text": "Eu vou gostosão pro são joão da escola", "member_id": "ramon-001"},
    {"id": "quote-003", "text": "Não sei como responder sua cantada, vou perguntar pro chat gpt", "member_id": "felipe-005"},
    {"id": "quote-004", "text": "Meu amigo, ligue o foda-se e pronto", "member_id": "ph-002"},
    {"id": "quote-005", "text": "Vai tomar no cu Davi", "member_id": "julliano-003"},
    {"id": "quote-006", "text": "E essa gameplay", "member_id": "italo-004"}
]


async def seed_database():
    """Popula o banco de dados com dados iniciais se estiver vazio"""
    
    # Verificar se já existem membros
    try:
        existing_members = await db.members.count_documents({})
        
        if existing_members == 0:
            print("🌱 Banco de dados vazio. Populando com dados iniciais...")
            
            # Inserir membros
            for member in MEMBERS_DATA:
                member['created_at'] = "2024-01-01T00:00:00"
                await db.members.insert_one(member)
            print(f"✅ {len(MEMBERS_DATA)} membros adicionados")
            
            # Inserir citações
            for quote in QUOTES_DATA:
                quote['created_at'] = "2024-01-01T00:00:00"
                await db.quotes.insert_one(quote)
            print(f"✅ {len(QUOTES_DATA)} citações adicionadas")
            
            print("✨ Banco de dados populado com sucesso!")
        else:
            print(f"ℹ️  Banco de dados já contém {existing_members} membros. Seed não necessário.")
            
    except Exception as e:
        print(f"❌ Erro ao conectar ou inserir dados: {e}")


if __name__ == "__main__":
    asyncio.run(seed_database())
