from flask import Blueprint, request, jsonify
from .models import DNA, db
from .utils import is_mutant

bp = Blueprint('routes', __name__)

@bp.route('/mutant/', methods=['POST'])
def mutant():
    data = request.json
    dna = data.get("dna", [])
    if not dna or not isinstance(dna, list):
        return jsonify({"error": "Invalid DNA format"}), 400

    sequence = ",".join(dna)  # Combina el ADN en un solo string
    existing_dna = DNA.query.filter_by(sequence=sequence).first()

    if existing_dna:  # Si ya está en la base de datos
        if existing_dna.is_mutant:
            return jsonify({"message": "Mutant"}), 200
        return jsonify({"message": "Human"}), 403

    # Analiza si es mutante
    mutant_result = is_mutant(dna)
    new_dna = DNA(sequence=sequence, is_mutant=mutant_result)
    db.session.add(new_dna)
    db.session.commit()

    if mutant_result:
        return jsonify({"message": "Mutant"}), 200
    return jsonify({"message": "Human"}), 403


@bp.route('/stats', methods=['GET'])
def stats():
    mutant_count = DNA.query.filter_by(is_mutant=True).count()
    human_count = DNA.query.count()
    ratio = mutant_count / human_count if human_count > 0 else 0

    return jsonify({
        "count_mutant_dna": mutant_count,
        "count_human_dna": human_count,
        "ratio": ratio
    }), 200
