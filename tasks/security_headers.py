# J3 Ex 13 : en-tetes de securite (corrige les alertes ZAP)
CSP = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https:; "
    "style-src 'self' 'unsafe-inline' https:; "
    "img-src 'self' data: https:; "
    "font-src 'self' https: data:; "
    "connect-src 'self'; "
    "frame-ancestors 'none'; "
    "form-action 'self'; "
    "base-uri 'self'; "
    "object-src 'none'"
)


class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", CSP)
        response.setdefault("Referrer-Policy", "same-origin")
        response.setdefault(
            "Permissions-Policy", "geolocation=(), microphone=(), camera=()"
        )
        response.setdefault("X-Content-Type-Options", "nosniff")
        response.setdefault("Cross-Origin-Opener-Policy", "same-origin")
        response.setdefault("Cache-Control", "no-store")
        return response
