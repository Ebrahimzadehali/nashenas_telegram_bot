from types import SimpleNamespace
from src.utils.keyboard import create_keyboard
import emoji



keys = SimpleNamespace(
    random_connect = ':grinning_face: Random Connect',
    settings = ':gear: Settings',
)



keyboards = SimpleNamespace(
    main=create_keyboard(keys.random_connect, keys.settings)
)