# Fix harmonic_mean()

`harmonic_mean()` in `habitat/calc.py` should return the harmonic mean (reciprocal average), not the arithmetic mean.

## Expected

```python
harmonic_mean([1.0, 2.0, 4.0])  # → 12/7 ≈ 1.714285714
```

## Failing test

```bash
pytest tests/test_calc.py::test_harmonic_mean -x
```