from langchain_openai import ChatOpenAI
from typing import Any, Dict, List, Optional, Union

class CustomChatOpenAI(ChatOpenAI):
    """Clase personalizada que extiende ChatOpenAI para trabajar con el modelo o4-mini.
    Esta clase sobrescribe el método _stream para eliminar el parámetro 'stop' que no es
    compatible con el modelo o4-mini.
    """
    
    def _stream(
        self,
        messages: List[Dict[str, Any]],
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> Any:
        """Sobrescribe el método _stream para eliminar el parámetro 'stop' cuando se usa el modelo o4-mini."""
        # Si el modelo es o4-mini, ignoramos el parámetro stop
        if self.model_name == "o4-mini" and "stop" in kwargs:
            del kwargs["stop"]
        
        # Llamamos al método original pero sin el parámetro stop para o4-mini
        if self.model_name == "o4-mini":
            return super()._stream(messages, stop=None, **kwargs)
        else:
            return super()._stream(messages, stop=stop, **kwargs)