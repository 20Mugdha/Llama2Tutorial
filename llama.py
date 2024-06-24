
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/m_ugdha/LLAMA2Tutorial/workflows/workflow-03a4e2"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="d1ab22a13eee487e98c858e124e3aad0"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
