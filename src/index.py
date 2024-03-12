from flask import Flask, render_template, request
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

app = Flask(__name__)

system_prompt = (
    "You are an expert coder in MermaidJS who only returns proper MermaidJS."
)
llm_template = "Take the following description and return only the proper MermaidJS. Do not write explanations. \n\nDescription:`{description}`\n\nMarkup:"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        diagram_description = request.form["diagramDescription"]

        # do inference here
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("user", llm_template),
            ]
        )

        model = ChatNVIDIA(model="llama2_70b")

        chain = (
            {
                "description": RunnablePassthrough(),
            }
            | prompt
            | model
            | StrOutputParser()
        )

        inferred_diagram_text = chain.invoke(
            {
                "description": diagram_description,
            }
        )

        inferred_diagram_text = inferred_diagram_text.lstrip("```mermaid")
        inferred_diagram_text = inferred_diagram_text.rstrip("```")

        return render_template(
            "index.html",
            diagramDescription=diagram_description,
            inferredDiagramText=inferred_diagram_text,
        )

    return render_template("index.html")
