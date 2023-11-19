from fastapi import Request
import logging
from logging.handlers import TimedRotatingFileHandler
import os


class APILogger:
    def __init__(self, name: str, log_directory: str = "logs", backup_count: int = 7):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        os.makedirs(log_directory, exist_ok=True)
        log_file_path = os.path.join(log_directory, f"{name}.log")

        handler = TimedRotatingFileHandler(
            log_file_path,
            when="midnight",
            interval=1,
            backupCount=backup_count
        )
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    async def log_request(self, request: Request, call_next):
        self.logger.info(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        self.logger.info(f"Request completed: {response.status_code}")
        return response
