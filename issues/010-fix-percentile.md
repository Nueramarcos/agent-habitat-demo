# Fix percentile()

`percentile()` in `habitat/calc.py` must use linear interpolation, not always return the median.

## Expected

```python
percentile([1.0, 2.0, 3.0, 4.0], 25.0)  # → 1.75
```

## Failing test

```bash
pytest tests/test_calc.py::test_percentile_p25 -x
```