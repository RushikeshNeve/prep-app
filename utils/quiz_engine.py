"""Quiz helpers for scoring and state updates."""

from utils.data import TopicContent


def evaluate_quiz(topic: TopicContent, selected_indices: list[int]) -> tuple[int, int, list[bool]]:
    correct_flags = []
    for idx, question in enumerate(topic.quiz_questions):
        chosen = selected_indices[idx] if idx < len(selected_indices) else -1
        correct_flags.append(chosen == question.answer_index)
    score = sum(correct_flags)
    total = len(topic.quiz_questions)
    return score, total, correct_flags


def update_best_score(state, topic_key: str, score: int, total: int) -> None:
    best = state["quiz_scores"].get(topic_key, 0)
    pct = round((score / total) * 100)
    if pct > best:
        state["quiz_scores"][topic_key] = pct
