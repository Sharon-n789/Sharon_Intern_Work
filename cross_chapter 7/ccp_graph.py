from graphviz import Digraph

class IPCC_CCP7_Graph:
    def __init__(self):
        # Initialize the Digraph object
        self.dot = Digraph("IPCC_CCP7_Structure", format="svg")
        self.dot.attr(rankdir="LR")  # Left-to-Right layout
        self.dot.attr("node", shape="ellipse", style="filled", color="lightgreen")

    def create_ccp7_structure(self):
        # Main CCP7 structure
        self.dot.node("CCP7", "Cross-Chapter Paper 7: Tropical Forests", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/")

        # Sections of CCP7
        sections = {
            "ExecSummary": ("Executive Summary", "https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/#exec-summary"),
            "Authors": ("Authors", "https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/#authors"),
            "Figures": ("Figures", "https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/#figures"),
            "Citations": ("How to Cite", "https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/#how-to-cite"),
            "FullReport": ("Full Report", "https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/full-report/"),
        }

        # Add nodes for each section
        for key, (label, url) in sections.items():
            self.dot.node(key, label, URL=url)

        # Connect sections to the main CCP7 node
        for key in sections.keys():
            self.dot.edge("CCP7", key)

    def render_graph(self):
        # Render the graph
        self.dot.render("ipcc_ccp7_structure", view=True)

# Instantiate the class and create the graph
ccp7_graph = IPCC_CCP7_Graph()
ccp7_graph.create_ccp7_structure()
ccp7_graph.render_graph()
