# J3 Ex 13 : en-tetes de securite (corrige les alertes ZAP : CSP, Referrer, Permissions-Policy)
class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault(
            "Content-Security-Policy",
            "default-src 'self' 'unsafe-inline' https: data:",
        )
        response.setdefault("Referrer-Policy", "same-origin")
        response.setdefault(
            "Permissions-Policy", "geolocation=(), microphone=(), camera=()"
        )
        response.setdefault("X-Content-Type-Options", "nosniff")
        return response
