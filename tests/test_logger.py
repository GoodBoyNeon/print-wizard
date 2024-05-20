from printwizard import Logger

logger = Logger({
    "include_timestamp": True,
    "include_status": False,
})

logger.success("Success Statement", {
    "include_timestamp": True,
})
logger.info("Success Statement")
logger.warn("Success Statement", {
    "include_timestamp": True,
})
logger.error("Success Statement")
