#!/usr/bin/python
import csv, sys, math, operator, re, os

try:
	filename = sys.argv[1]
except:
	print "\nPlease input a valid CSV filename.\n"
	print "Format: python scriptname filename.\n"
	exit()

newCsv = []
newFile = open('magento_export.csv', 'wb') #wb for windows, else you'll see newlines added to csv

# open the file from console arguments
with open(filename, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		newCsv.append(row)

# initialize csv writer
writer = csv.writer(newFile)
# write magento's headers
header_row1 = ('attribute_set', 'websites', 'category_ids','sku', 'product_id', 'has_options', 'product_name', 'name', 'meta_title',
	'description', 'meta_description', 'short_description', 'Type', 'meta_keyword', 'Pricing', 'gallery', 'price', 'weight',
	'image', 'small_image', 'thumbnail', 'image_label', 'small_image_label', 'thumbnail_label', 'gift_message_available', 'page_layout',
	'options_container', 'store', 'prodtype', 'status', 'visibility', 'enable_googlecheckout', 'tax_class_id', 'qty', 'min_qty',
	'use_config_min_qty', 'is_qty_decimal', 'backorders', 'is_in_stock', 'notify_stock_qty', 'use_config_notify_stock_qty',
	'manage_stock', 'use_config_manage_stock', 'stock_status_changed_auto', 'use_config_qty_increments', 'qty_increments', 
	'use_config_enable_qty_inc', 'enable_qty_increments', 'is_decimal_divided', 'stock_status_changed_automatically', 'use_config_enable_qty_increments',
	'store_id', 'product_type_id')

writer.writerow(header_row1)

for item in newCsv:
	attribute_set = 'Default'
	websites = 'buffalohistory'
	category_ids = item['category_ids']
	sku = item['sku']
	product_id = item['product_id']
	has_options = "1"
	product_name = item['product_name']
	name = product_name
	meta_title = product_name
	description = item['description']
	
	try:
		meta_description = item['meta_description']
	except:
		meta_description = ""

	try:
		short_description = item['short_description']
	except:
		short_description = ""	

	type = item['Type']

	meta_keyword = item['meta_keyword']
	pricing = ""

	try:
		gallery = item['gallery']
	except:
		gallery = ""

	try:	
		price = item['price']
	except:
		price = ""

	weight = "1"
	image = item['image']
	small_image = image
	thumbnail = image
	image_label = item['image_label']
	small_image_label = image_label
	thumbnail_label = image_label
	gift_message_available = 'No'
	page_layout ='No layout updates'
	options_container = 'Product Info Column'
	store = 'admin'
	prodtype = 'simple'
	status = 'Enabled'
	visibility = 'Catalog, Search'
	enable_googlecheckout = 'Yes'
	tax_class_id = 'Taxable Goods'
	qty = "100"
	min_qty = "0"
	use_config_min_qty = "1"
	is_qty_decimal = "0"
	backorders = "0"
	is_in_stock = "1"
	notify_stock_qty = "0"
	use_config_notify_stock_qty = "1"
	manage_stock = "0"
	use_config_manage_stock = "1"
	stock_status_changed_auto = "0"
	use_config_qty_increments = "1"
	qty_increments  = "0"
	use_config_enable_qty_inc = "1"
	enable_qty_increments = "0"
	is_decimal_divided = "0"
	stock_status_changed_automatically = "0"
	use_config_enable_qty_increments = "1"
	store_id = "0"
	product_type_id = "simple"

	write_tuple = (attribute_set, websites, category_ids,sku,product_id,has_options,product_name,name,meta_title,
		description, meta_description, short_description, type, meta_keyword, pricing, gallery, price, weight,
		image, small_image, thumbnail, image_label, small_image_label, thumbnail_label, gift_message_available, page_layout,
		options_container, store, prodtype, status, visibility, enable_googlecheckout, tax_class_id, qty, min_qty,
		use_config_min_qty, is_qty_decimal, backorders, is_in_stock, notify_stock_qty, use_config_notify_stock_qty,
		manage_stock, use_config_manage_stock, stock_status_changed_auto, use_config_qty_increments, qty_increments, 
		use_config_enable_qty_inc, enable_qty_increments, is_decimal_divided, stock_status_changed_automatically, use_config_enable_qty_increments,
		store_id, product_type_id)

	writer.writerow(write_tuple)

# initialize csv writer
writer = csv.writer(newFile)
newFile.close()












