import xml.etree.ElementTree as ET
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    tree = ET.parse('pom.xml')
    root = tree.getroot()
    for xml in root:
        if "groupId" in xml.tag:
            group = xml.tag
        if "artifactId" in xml.tag:
            artifact = xml.tag

    group_id = root.find(group)

    artifact_id = root.find(artifact)
    if "-" in artifact_id.text:
        artifact_id_text = artifact_id.text.replace("-","")
    else:  
        artifact_id_text = artifact_id.text 

    package= f"{group_id.text}.{artifact_id.text}"
    path_code_directory= f"src.main.java.{group_id.text}.{artifact_id_text}"
    path_test_code_directory= f"src.test.java.{group_id.text}.{artifact_id_text}"
    
    metadata.inputs['package']=package
    metadata.inputs['path_code_directory']=path_code_directory
    metadata.inputs['path_test_code_directory']=path_test_code_directory

    return metadata