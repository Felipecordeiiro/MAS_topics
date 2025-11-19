import sys
import warnings

from crew import Station

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():

    inputs = {
        "occurrence_report": (
            "On November 19, 2025, at 5:30 p.m., at 450 Girassóis Street, Jardim neighborhood,"
            "the victim, Ms. Ana Silva, reported the theft of her electric bicycle."
            "The bicycle was locked in the garage. There was no visible break-in,"
            "suggesting that the criminal used a fake key or had prior access."
            "The bicycle is blue, brand Specialized. The victim attached photos"
            "of the bicycle and the intact lock. There is a record of a similar bicycle"
            "theft on the same street 3 months ago (BO-2025/12345)."
        )
    }

    try:
        Station().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"Um erro ocorreu enquanto rodava o crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Police Station",
    }
    try:
        Station().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"Um erro ocorreu enquanto rodava o crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Station().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"Um erro ocorreu enquanto rodava o crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Police Station",
    }

    try:
        Station().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"Um erro ocorreu enquanto rodava o crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("Nenhum payload trigger foi fornecido. Por favor forneça um JSON payload como argumento.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Payload JSON fornecido como argumento é inválido")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "message": ""
    }

    try:
        result = Station().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"Um erro ocorreu enquanto rodava o crew: {e}")
    
run()