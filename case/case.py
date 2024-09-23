#!/usr/bin/env python3

# vpype read default/swoon-Edge_Cuts_LEFT.svg linemerge --tolerance 3mm linesort reloop linesimplify write default/swoon-Edge_Cuts_LEFT_vpype.svg
    
from build123d import *
# from ocp_vscode import show_object as show, set_port

# set_port(3939)

with BuildPart() as void:
    with BuildSketch(Plane.XY.offset(2 * MM)) as edge_cuts:
        with BuildLine() as line:
            svg = import_svg("case/swoon_edges_vpype.svg")
            add(svg)
        make_face()
    extrude(amount = 4 * MM)

with BuildPart() as case:
    with BuildSketch() as outline:
        add(edge_cuts)
        offset(amount=2 * MM, min_edge_length=3 * MM) 
    extrude(amount=6 * MM)

    add(void, mode=Mode.SUBTRACT)
    # top_face = case.faces().sort_by(Axis.Z)[-1]
    # fillet(top_face.edges(), radius=0.3 * MM)

# show(case)
export_step(case.part, file_path="case/case.step")
export_stl(case.part, file_path="case/case.stl")