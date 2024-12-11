def main():
    # Load the configuration file
    config_file = "config.cfg"
    settings = fix.SessionSettings(config_file)
    application = Application()

    # Create store and log factories
    store_factory = fix.FileStoreFactory(settings)
    log_factory = fix.FileLogFactory(settings)

    # Initialize the socket initiator (FIX client)
    initiator = fix.SocketInitiator(application, store_factory, settings, log_factory)

    try:
        initiator.start()
        print("FIX client started. Press Enter to exit.")
        input()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        initiator.stop()
        print("FIX client stopped.")

if __name__ == "__main__":
    main()