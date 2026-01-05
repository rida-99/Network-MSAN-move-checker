from flask import Blueprint, render_template, request
from app.utils.predictor import can_move_ne

main_bp = Blueprint("main", __name__)

# Route for the home page
@main_bp.route("/")
def index():
    return render_template("index.html")

# Route for MSAN single migration page
@main_bp.route("/msan-single-migration")
def msan_single_migration():
    return render_template("check-msan-single.html")

# Route for MSAN dual migration page
@main_bp.route("/msan-dual-migration")
def msan_dual_migration():
    return render_template("check-msan-dual.html")

# Route for MSAN migration check processing
@main_bp.route("/msan-migration-check", methods=["POST"])
def check():
    my_bw = float(request.form["my_bw"])
    my_charge = float(request.form["my_charge"])
    
    peer1_bw = float(request.form["peer1_bw"])
    peer1_charge = float(request.form["peer1_charge"])
    
    peer2_bw = float(request.form["peer2_bw"])
    peer2_charge = float(request.form["peer2_charge"])

    result = can_move_ne(my_bw, my_charge, peer1_bw, peer1_charge, peer2_bw, peer2_charge)

    return render_template("result.html", result=result)
