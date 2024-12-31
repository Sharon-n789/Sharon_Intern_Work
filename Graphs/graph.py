from graphviz import Digraph

class IPCC_AR6_Graphs:
    def __init__(self):
        # Initialize the Digraph objects for both graphs
        self.ipcc_dot = Digraph("IPCC_Structure", format="svg")  # Use SVG for clickable links
        self.ar6_dot = Digraph("AR6_WGII", format="svg")

        # Set common attributes for both graphs
        self.ipcc_dot.attr(rankdir="LR")  # Left-to-Right layout for IPCC
        self.ar6_dot.attr(rankdir="LR")   # Left-to-Right layout for AR6
        self.ipcc_dot.attr("node", shape="ellipse", style="filled", color="lightyellow")
        self.ar6_dot.attr("node", shape="ellipse", style="filled", color="lightblue")

    def create_ipcc_structure(self):
        # Main IPCC structures with URLs
        self.ipcc_dot.node("IPCC", "IPCC", URL="https://www.ipcc.ch/")
        self.ipcc_dot.node("Plenary", "Plenary", URL="https://www.ipcc.ch/about/plenary/")
        self.ipcc_dot.node("Bureau", "Bureau", URL="https://www.ipcc.ch/about/bureau/")
        self.ipcc_dot.node("Secretariat", "Secretariat", URL="https://www.ipcc.ch/about/secretariat/")
        self.ipcc_dot.node("Working Group I", "Working Group I", URL="https://www.ipcc.ch/working-group/wg1/")
        self.ipcc_dot.node("Working Group II", "Working Group II", URL="https://www.ipcc.ch/working-group/wg2/")
        self.ipcc_dot.node("Working Group III", "Working Group III", URL="https://www.ipcc.ch/working-group/wg3/")
        self.ipcc_dot.node("Task Force", "Task Force", URL="https://www.ipcc.ch/taskforce/")
        self.ipcc_dot.node("Reports", "Reports", URL="https://www.ipcc.ch/reports/")

        # Add edges for main structure
        self.ipcc_dot.edges([
            ("IPCC", "Plenary"),
            ("IPCC", "Bureau"),
            ("IPCC", "Secretariat"),
            ("IPCC", "Working Group I"),
            ("IPCC", "Working Group II"),
            ("IPCC", "Working Group III"),
            ("IPCC", "Task Force"),
            ("IPCC", "Reports")
        ])

    def create_ar6_structure(self):
        # Main Report Structure with URLs
        self.ar6_dot.node("AR6", "AR6 WGII", URL="https://www.ipcc.ch/report/ar6/wg2/")
        self.ar6_dot.node("SPM", "Summary for Policymakers", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/summary-for-policymakers/")
        self.ar6_dot.node("TS", "Technical Summary", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/technical-summary/")
        self.ar6_dot.node("FR", "Full Report", URL="https://www.ipcc.ch/report/ar6/wg2/")
        self.ar6_dot.node("CP", "Chapters", URL="https://www.ipcc.ch/report/ar6/wg2/")
        self.ar6_dot.node("CCP", "Cross Chapters", URL="https://www.ipcc.ch/report/ar6/wg2/")

        # Connect summaries and full report to AR6 WGII
        self.ar6_dot.edges([("AR6", "SPM"), ("AR6", "TS"), ("AR6", "FR"), ("AR6", "CP"), ("AR6", "CCP")])

    def render_graphs(self):
        # Render both graphs
        self.ipcc_dot.render("ipcc_structure", view=True)
        self.ar6_dot.render("ar6_wgii_summary", view=True)


# Instantiate the class and use its methods to create and render both graphs
graphs = IPCC_AR6_Graphs()
graphs.create_ipcc_structure()
graphs.create_ar6_structure()
graphs.render_graphs()
