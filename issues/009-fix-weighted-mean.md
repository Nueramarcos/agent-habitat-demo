# Fix weighted_mean()

`weighted_mean()` in `habitat/calc.py` must respect weights, not return a plain arithmetic mean.

## Expected

```python
weighted_mean([1.0, 2.0, 3.0], [1.0, 1.0, 8.0])  # → 2.9
```

## Failing test

```bash
pytest tests/test_calc.py::test_weighted_mean -x
```