from botbuilder.core import BotFrameworkAdapter, TurnContext, MessageFactory, BotFrameworkAdapterSettings
from botbuilder.schema import Activity, ActivityTypes
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from dotenv import dotenv_values, load_dotenv
import os

config = dotenv_values(".env")
connect = load_dotenv()

router = APIRouter(tags=["ChatBot"])


app_settings = BotFrameworkAdapterSettings(
    app_id= os.getenv('AZURE_APP_ID'),
    app_password=os.getenv('AZURE_APP_PASSWORD')
)

def get_bot_adapter():
    return BotFrameworkAdapter(app_settings)

# Your Bot logic
class MyBot:
    async def on_turn(self, turn_context: TurnContext):
        if turn_context.activity.type == ActivityTypes.message:
            await turn_context.send_activity(MessageFactory.text(f"You said: {turn_context.activity.text}"))

# Instantiate the Bot
bot = MyBot()

# Handle incoming messages
async def handle_activity(request: Request, adapter: BotFrameworkAdapter = Depends(get_bot_adapter)):
    body = await request.body()
    try:
        await adapter.process_activity(body, request.headers["Authorization"], bot.on_turn)
        return JSONResponse(content={}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Define the endpoint for receiving messages
@router.post("/api/messages")
async def messages_endpoint(request: Request, response: JSONResponse = Depends(handle_activity)):
    return response
