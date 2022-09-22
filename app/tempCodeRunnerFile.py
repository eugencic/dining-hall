dining_hall_thread = Thread(target=lambda: app.run(host = '0.0.0.0', port = 3000, debug = False, use_reloader = False), daemon = True)
    dining_hall_thread.start()
    # Create thread Client
    client_thread = Client()
    # Add the thread to the array
    threads.append(client_thread)
    for _, waiter in enumerate(waiters):
        # Create Waiter threads
        waiter_thread = Waiter(waiter)
        # Add the thread to the list
        threads.append(waiter_thread)
    # Start the threads
    for thread in threads:
        thread.start()
    # Wait for the threads to complete    
    for thread in threads:
        thread.join()