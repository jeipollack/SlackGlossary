from subprocess import check_output


def register_glossary_commands(app):
    @app.command("/glossary")
    def define_acronym(ack, respond, command):
        ack()
        acronym = check_output(
            [
                "python3",
                "/opt/SlackGlossaryBot/SlackGlossaryBot/glossary/glossary.py",
                "-g",
                "/opt/SlackGlossaryBot/SlackGlossaryBot/glossary/glossary.json",
                f"{command['text']}",
            ]
        )
        definition = (
            f"{command['text']} => " + acronym.decode("utf-8").strip().split("\n")[0]
        )
        respond(definition)
