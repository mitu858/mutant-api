from flask import Blueprint, request, jsonify
from .models import DNA, db
from .utils import is_mutant

bp = Blueprint('routes', __name__)

@bp.route('/mutant/', methods=['POST'])
def mutant():
    try:
        data = request.get_json()
        dna = data.get("dna")
        
        # Validación del formato de entrada
        if not dna or not isinstance(dna, list):
            return jsonify({"error": "Formato inválido. 'dna' debe ser una lista de cadenas."}), 400

        # Validación de que es una matriz NxN
        n = len(dna)
        if not all(isinstance(row, str) and len(row) == n for row in dna):
            return jsonify({"error": "La secuencia de ADN debe ser una matriz NxN con cadenas de igual longitud."}), 400

        # Validación de caracteres válidos
        valid_chars = {'A', 'T', 'C', 'G'}
        for row in dna:
            if any(char not in valid_chars for char in row):
                return jsonify({"error": "La secuencia de ADN contiene caracteres inválidos. Solo se permiten 'A', 'T', 'C', 'G'."}), 400

        # Verificar si es mutante
        if is_mutant(dna):
            return jsonify({"message": "Mutante detectado."}), 200
        else:
            return jsonify({"message": "No es un mutante."}), 403
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


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
