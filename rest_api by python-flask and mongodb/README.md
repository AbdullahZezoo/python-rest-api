Reuirements
______

install python 3.6 or later
install Postman

run in the terminal the following command:
		pip install -r requirements.txt
			
run task.py 

it will Run on http://127.0.0.1:5000/	
		
		
Coffee Database
_______________

has two documents : 
1-coffee_machines
2-coffee_products



to get_all_coffee --> http://127.0.0.1:5000/coffee_machines   --> function get_all_coffee  

to get specific coffe by product_type --> http://127.0.0.1:5000/coffee_machines/<product_type> -- function get_coffee -- product_type {small_machine, large_machine, espresso_machine}

to get coffee by product_type and water_line --> http://127.0.0.1:5000/coffee_machines/<product_type>/<water_line> -- function get_coffee_filter -- water_line {True, False}

to get all coffee prods http://127.0.0.1:5000/coffee_pods  --> function get_all_pods 

to get coffee by product_type http://127.0.0.1:5000/coffee_machines/<product_type>  -- function get_pods -- product_type {small_machine_pod, large_machine_pod, espresso_machine_pod}

to get coffee by flavor http://127.0.0.1:5000/coffee_machines/<product_type>/<coffee_flavor> -- function get_pods_filter -- coffee_flavor {vanilla, mocha, psl, caramel, hazelnut}

to get coffee by pack_size http://127.0.0.1:5000/coffee_machines/<product_type>/<coffee_flavor>/<pack_size> -- function get_pods_filter2 -- pack_size {1dozen, 3dozen, 5dozen, 7dozen}




