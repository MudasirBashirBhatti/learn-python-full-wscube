import logging
# ...............Custom logging............

logging.basicConfig(
    filename='3. coding start/15_logging/app.log', #file name
    level=logging.DEBUG, #minimal level(if set to LEVEL the debugs will not print)
    format="%(asctime)s - %(levelname)s - %(message)s", #custom message
    datefmt="%Y-%m-%d %H:%M:%S", #custom date format
    style='%'
    )

logging.info("saved to file")