#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    _best_score = 0
    _best_key = None
    for key, value in a_dictionary.items():
        if value > _best_score:
            _best_key = key
            _best_score = value

    return _best_key
