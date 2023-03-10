from gs_web_app import create_app

app = create_app({
    "DEBUG": True,
    "SECRET_KEY": "dev",
})

if __name__ == "__main__":
    app.run()
