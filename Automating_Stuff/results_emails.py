import smtplib
import ssl
import pandas as pd
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

### SETUP ### 
# Do not use email as a name for neither the file or any functions or variables to avoid conflicts with the email module

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "agbonorino21@gmail.com" # Email to send from
email_to = "agbonorino21@gmail.com" # Email to send to

pswd = "vftmpdokgxgqssit"       # App password for gmail

simple_email_context = ssl.create_default_context()

### WORK ###
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx

# empty lists to store logs and images paths
logs = []
images_paths = []

# Load the 'brain_networks' dataset from seaborn
data = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

# Calculate the correlation matrix
corr_matrix = data.corr()

# Create a network graph from the correlation matrix
threshold = 0.6  # You can adjust this threshold value based on your analysis
graph = nx.from_pandas_adjacency(corr_matrix, create_using=nx.Graph())

# Filter edges based on the threshold value
filtered_edges = [(node1, node2) for node1, node2, weight in graph.edges(data='weight') if abs(weight) >= threshold]
graph_filtered = nx.Graph(filtered_edges)

# Print the number of nodes and edges in the filtered graph
log1 = f"Filtered graph: {graph_filtered.number_of_nodes()} nodes, {graph_filtered.number_of_edges()} edges"
logs.append(log1)

# Calculate average clustering coefficient and shortest path length
avg_clustering_coefficient = nx.average_clustering(graph_filtered)
log2 = f"Average Clustering Coefficient: {avg_clustering_coefficient:.4f}"
logs.append(log2)

# Calculate the shortest path length for connected components
shortest_path_lengths = []
for component in nx.connected_components(graph_filtered):
    subgraph = graph_filtered.subgraph(component)
    shortest_path_lengths_subgraph = nx.average_shortest_path_length(subgraph)
    shortest_path_lengths.append(shortest_path_lengths_subgraph)

avg_shortest_path_length = np.mean(shortest_path_lengths)
log3 = f"Average Shortest Path Length: {avg_shortest_path_length:.4f}"
logs.append(log3)

# Visualize the correlation matrix and save as png
fig1 = plt.figure(figsize=(20, 15))
plt.matshow(corr_matrix)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=10)
plt.title('Correlation Matrix', fontsize=12)
corr_matrix_fig_path = "Brain_Networks_CorrMatrix.png"
plt.savefig(corr_matrix_fig_path)
images_paths.append(corr_matrix_fig_path)

# (Add your NetworkX graphing code here.)

# Save the graph visualization as a PNG image
fig2 = plt.figure()
# Visualize the filtered graph
pos = nx.spring_layout(graph_filtered, seed=42)
nx.draw(graph_filtered, pos, node_size=50, node_color='skyblue', with_labels=False)
filtered_network_fig_path = 'brain_networks_filtered_graph.png'
plt.savefig(filtered_network_fig_path)
images_paths.append(filtered_network_fig_path)


### EMAIL ###
# function to write logs given list of strings and return the formatted string
def write_logs(logs):
    '''Returns a formatted string from a list of strings'''
    message = ""
    
    for log in logs:
        message += f"{log} - finished running at {datetime.now()} \n"
    
    return message

try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")
    
    message = write_logs(logs)

    msg_logs = MIMEMultipart('mixed')
    msg_logs["From"] = email_from
    msg_logs["To"] = email_to
    msg_logs["Subject"] = "Email Logs"
    
    # build body of email
    body = MIMEText(message, "plain")
    msg_logs.attach(body)
    
    # attach images to the email
    for image_path in images_paths:
        with open(image_path, "rb") as image:
            attachment = MIMEApplication(image.read(), _subtype="png")
            attachment.add_header('Content-Disposition','attachment', filename=image_path)
            msg_logs.attach(attachment)
    
    parsed_msg = msg_logs.as_string()
    
    # send email
    print("Sending email...")
    
    TIE_server.sendmail(email_from, email_to, parsed_msg)
    
    print('Logs emailed succesfully')
    
# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()
    