from app import application

os.environ["STRIPE_PUBLISHABLE"] = "pk_test_rGhd3iNEhAPQYfQrfxxWCEB3"
os.environ["STRIPE_SECRET"] = "sk_test_E1m4uFrhbx174r7pMMpq2Ckl"

if __name__ == "__main__":
    application.run()
