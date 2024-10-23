"""
    log programming...
"""

import logging

def div(a, b):
    try:
        a / b ## error must be before good log....
        logging.info(f"succesful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as exc:
        logging.error(f"division by zero {a} / {b}", exc_info=True) ## exc_info - send information about exception to log system


if __name__ == "__main__":

    """
        log save data to files...
    """
    logging.basicConfig(level=logging.INFO, filemode="w", filename="project.log",
                        format="%(asctime)s | %(module)s | %(levelname)s | %(message)s")

    print(div(3, 4))
    print(div(3, 0))

    """
        log has 5 levels...
    """
    logging.warning("->Warning: ...")   
    logging.error(" ->Error: ...")
    logging.critical(" ->Critical error: ...")
    logging.debug(" ->Debug: ...")    
    logging.info(" ->Info: ...")



