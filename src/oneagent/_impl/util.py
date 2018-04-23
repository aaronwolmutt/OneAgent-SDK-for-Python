import sys

if hasattr(lambda: None, '__qualname__'):
    def getqualname(val):
        return val.__qualname__
else:
    def getqualname(val):
        return val.__name__

def getfullname(val):
    """Get the module-qualified name of type or function val."""
    return (val.__module__ or '<UNKNOWN_MODULE>') + '.' + getqualname(val)

def error_from_exc(nsdk, tracer_h, e_val=None, e_ty=None):
    """Attach appropriate error information to tracer_h.

    If e_val and e_ty are None, the current exception is used."""

    if not tracer_h:
        return

    if e_ty is None and e_val is None:
        e_ty, e_val = sys.exc_info()[:2]
    if e_ty is None and e_val is not None:
        e_ty = type(e_val)
    nsdk.tracer_error(tracer_h, getfullname(e_ty), str(e_val))
