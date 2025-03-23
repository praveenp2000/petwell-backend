INSERT INTO petwell_customer (name, email, password, address, phone) VALUES
('John Doe', 'john@example.com', 'pass123', '123 Main St', '1234567890'),
('Jane Smith', 'jane@example.com', 'pass456', '456 Oak St', '2345678901'),
('Alice Johnson', 'alice@example.com', 'pass789', '789 Pine St', '3456789012'),
('Bob Brown', 'bob@example.com', 'passabc', '101 Maple St', '4567890123'),
('Charlie White', 'charlie@example.com', 'passdef', '202 Birch St', '5678901234'),
('David Black', 'david@example.com', 'passghi', '303 Cedar St', '6789012345'),
('Eve Green', 'eve@example.com', 'passjkl', '404 Elm St', '7890123456'),
('Frank Grey', 'frank@example.com', 'passmno', '505 Spruce St', '8901234567'),
('Grace Blue', 'grace@example.com', 'passpqr', '606 Ash St', '9012345678'),
('Hank Red', 'hank@example.com', 'passstu', '707 Willow St', '0123456789');


INSERT INTO petwell_pet (name, age, gender, animal, breed, color, customer_id_id) VALUES
('Buddy', 2, 'Male', 'Dog', 'Labrador', 'Yellow', 1),
('Luna', 3, 'Female', 'Cat', 'Persian', 'White', 2),
('Charlie', 1, 'Male', 'Dog', 'Beagle', 'Brown', 3),
('Max', 4, 'Male', 'Dog', 'Bulldog', 'Black', 4),
('Milo', 2, 'Male', 'Cat', 'Siamese', 'Gray', 5),
('Bella', 3, 'Female', 'Dog', 'Poodle', 'White', 6),
('Lucy', 1, 'Female', 'Cat', 'Maine Coon', 'Orange', 7),
('Rocky', 5, 'Male', 'Dog', 'German Shepherd', 'Black', 8),
('Coco', 2, 'Female', 'Cat', 'Bengal', 'Spotted', 9),
('Venece', 4, 'Female', 'Dog', 'Golden Retriever', 'Golden', 10);

INSERT INTO petwell_doctor (name, phone, qualification, email, password) VALUES
('Dr. Smith', '1112223333', 'DVM', ' ', 'docpass1'),
('Dr. Johnson', '2223334444', 'DVM', 'drjohnson@example.com', 'docpass2'),
('Dr. Brown', '3334445555', 'DVM', 'drbrown@example.com', 'docpass3'),
('Dr. Green', '4445556666', 'DVM', 'drgreen@example.com', 'docpass4'),
('Dr. White', '5556667777', 'DVM', 'drwhite@example.com', 'docpass5'),
('Dr. Black', '6667778888', 'DVM', 'drblack@example.com', 'docpass6'),
('Dr. Blue', '7778889999', 'DVM', 'drblue@example.com', 'docpass7'),
('Dr. Red', '8889990000', 'DVM', 'drred@example.com', 'docpass8'),
('Dr. Grey', '9990001111', 'DVM', 'drgrey@example.com', 'docpass9'),
('Dr. Yellow', '0001112222', 'DVM', 'dryellow@example.com', 'docpass10');


INSERT INTO petwell_service (name, cost, time) VALUES
('General Checkup', 50, '30 mins'),
('Vaccination', 75, '45 mins'),
('Surgery', 500, '2 hours'),
('Dental Cleaning', 100, '1 hour'),
('Grooming', 40, '1 hour'),
('Microchipping', 30, '20 mins'),
('Deworming', 25, '15 mins'),
('Emergency Treatment', 200, 'As needed'),
('X-ray', 150, '1 hour'),
('Ultrasound', 180, '1 hour');


INSERT INTO petwell_petservice (customer_id_id, service_id_id, pet_id_id, status) VALUES
(1, 1, 1, 'Completed'),
(2, 2, 2, 'Pending'),
(3, 3, 3, 'Completed'),
(4, 4, 4, 'Pending'),
(5, 5, 5, 'Completed'),
(6, 6, 6, 'Pending'),
(7, 7, 7, 'Completed'),
(8, 8, 8, 'Pending'),
(9, 9, 9, 'Completed'),
(10, 10, 10, 'Pending');

INSERT INTO petwell_adoption (breed, animal, color, age, description, image, gender, adopted) VALUES
('Labrador', 'Dog', 'Yellow', 2, 'Friendly and playful', 'img1.jpg', 'Male', false),
('Persian', 'Cat', 'White', 3, 'Fluffy and quiet', 'img2.jpg', 'Female', true),
('Beagle', 'Dog', 'Brown', 1, 'Energetic and loyal', 'img3.jpg', 'Male', false),
('Bulldog', 'Dog', 'Black', 4, 'Calm and protective', 'img4.jpg', 'Male', true),
('Siamese', 'Cat', 'Gray', 2, 'Curious and smart', 'img5.jpg', 'Male', false),
('Poodle', 'Dog', 'White', 3, 'Elegant and friendly', 'img6.jpg', 'Female', true),
('Maine Coon', 'Cat', 'Orange', 1, 'Large and affectionate', 'img7.jpg', 'Female', false),
('German Shepherd', 'Dog', 'Black', 5, 'Brave and strong', 'img8.jpg', 'Male', true),
('Bengal', 'Cat', 'Spotted', 2, 'Active and social', 'img9.jpg', 'Female', false),
('Golden Retriever', 'Dog', 'Golden', 4, 'Loving and intelligent', 'img10.jpg', 'Female', true);


INSERT INTO petwell_booking (doctor_id_id, customer_id_id, pet_id_id, date, slot, booking_type) VALUES
(1, 1, 1, '2025-03-10 10:00:00', 'Morning', 'Checkup'),
(2, 2, 2, '2025-03-11 14:00:00', 'Afternoon', 'Surgery'),
(3, 3, 3, '2025-03-12 09:30:00', 'Morning', 'Vaccination'),
(4, 4, 4, '2025-03-13 16:00:00', 'Evening', 'Dental Cleaning'),
(5, 5, 5, '2025-03-14 11:00:00', 'Morning', 'Grooming'),
(6, 6, 6, '2025-03-15 13:00:00', 'Afternoon', 'General Checkup'),
(7, 7, 7, '2025-03-16 09:00:00', 'Morning', 'Emergency Treatment'),
(8, 8, 8, '2025-03-17 15:00:00', 'Evening', 'X-ray'),
(9, 9, 9, '2025-03-18 10:30:00', 'Morning', 'Ultrasound'),
(10, 10, 10, '2025-03-19 12:00:00', 'Afternoon', 'Microchipping');

INSERT INTO petwell_health (pet_id_id, customer_id_id, date, description, prescription) VALUES
(1, 1, '2025-03-10 10:00:00', 'Routine checkup', 'Vitamin supplements'),
(2, 2, '2025-03-11 11:00:00', 'Vaccination', 'Rabies vaccine'),
(3, 3, '2025-03-12 12:00:00', 'Injury treatment', 'Painkillers'),
(4, 4, '2025-03-13 13:00:00', 'Skin allergy', 'Antihistamines'),
(5, 5, '2025-03-14 14:00:00', 'Dental cleaning', 'Oral rinse'),
(6, 6, '2025-03-15 15:00:00', 'Worming treatment', 'Deworming tablets'),
(7, 7, '2025-03-16 16:00:00', 'Eye infection', 'Antibiotic drops'),
(8, 8, '2025-03-17 17:00:00', 'Ear infection', 'Ear drops'),
(9, 9, '2025-03-18 18:00:00', 'Post-surgery checkup', 'Pain relief meds'),
(10, 10, '2025-03-19 19:00:00', 'Fever', 'Paracetamol'),
(1, 1, '2025-03-20 10:00:00', 'Weight loss', 'Nutritional diet'),
(2, 2, '2025-03-21 11:00:00', 'Fracture', 'Splinting'),
(3, 3, '2025-03-22 12:00:00', 'Vaccination', 'Booster shots'),
(4, 4, '2025-03-23 13:00:00', 'Stomach upset', 'Probiotics'),
(5, 5, '2025-03-24 14:00:00', 'Arthritis', 'Joint supplements'),
(6, 6, '2025-03-25 15:00:00', 'Gastro issues', 'Digestive enzymes'),
(7, 7, '2025-03-26 16:00:00', 'Skin rash', 'Topical cream'),
(8, 8, '2025-03-27 17:00:00', 'Limping', 'Pain relief'),
(9, 9, '2025-03-28 18:00:00', 'Dehydration', 'IV fluids'),
(10, 10, '2025-03-29 19:00:00', 'Post-op care', 'Antibiotics'),
(1, 1, '2025-03-30 10:00:00', 'Routine checkup', 'Multivitamins'),
(2, 2, '2025-03-31 11:00:00', 'Ear mites', 'Ear cleaning solution'),
(3, 3, '2025-04-01 12:00:00', 'Coughing', 'Cough syrup'),
(4, 4, '2025-04-02 13:00:00', 'Dietary imbalance', 'Special diet plan'),
(5, 5, '2025-04-03 14:00:00', 'Lethargy', 'Energy boosters'),
(6, 6, '2025-04-04 15:00:00', 'Eye checkup', 'Vision supplements'),
(7, 7, '2025-04-05 16:00:00', 'Vaccination', 'Annual shots');
INSERT INTO petwell_health (pet_id_id, customer_id_id, date, description, prescription) VALUES
(1, 1, '2025-03-10 10:00:00', 'Routine checkup', 'Vitamin supplements'),
(2, 2, '2025-03-11 11:00:00', 'Vaccination', 'Rabies vaccine'),
(3, 3, '2025-03-12 12:00:00', 'Injury treatment', 'Painkillers'),
(4, 4, '2025-03-13 13:00:00', 'Skin allergy', 'Antihistamines'),
(5, 5, '2025-03-14 14:00:00', 'Dental cleaning', 'Oral rinse'),
(6, 6, '2025-03-15 15:00:00', 'Worming treatment', 'Deworming tablets'),
(7, 7, '2025-03-16 16:00:00', 'Eye infection', 'Antibiotic drops'),
(8, 8, '2025-03-17 17:00:00', 'Ear infection', 'Ear drops'),
(9, 9, '2025-03-18 18:00:00', 'Post-surgery checkup', 'Pain relief meds'),
(10, 10, '2025-03-19 19:00:00', 'Fever', 'Paracetamol');


INSERT INTO petwell_seller (name, email, password) VALUES
('Tom Hardy', 'tom@example.com', 'sellpass1'),
('Emily Stone', 'emily@example.com', 'sellpass2'),
('Michael Keaton', 'michael@example.com', 'sellpass3'),
('Natalie Portman', 'natalie@example.com', 'sellpass4'),
('Chris Pratt', 'chris@example.com', 'sellpass5');


INSERT INTO petwell_product (seller_id_id, name, price, quantity, animal, producttype, rating, approved) VALUES
(1, 'Dog Shampoo', 15, 50, 'Dog', 'Grooming', 5, TRUE),
(2, 'Cat Litter', 20, 40, 'Cat', 'Hygiene', 4, TRUE),
(3, 'Bird Cage', 50, 10, 'Bird', 'Housing', 4, TRUE),
(4, 'Fish Tank Filter', 30, 20, 'Fish', 'Aquarium', 5, TRUE),
(5, 'Rabbit Hutch', 60, 5, 'Rabbit', 'Housing', 4, TRUE),
(1, 'Dog Food', 25, 100, 'Dog', 'Food', 5, TRUE),
(2, 'Cat Scratching Post', 35, 15, 'Cat', 'Furniture', 4, TRUE),
(3, 'Parrot Toys', 10, 30, 'Bird', 'Toys', 5, TRUE),
(4, 'Aquarium Heater', 40, 12, 'Fish', 'Aquarium', 5, TRUE),
(5, 'Hamster Wheel', 15, 25, 'Hamster', 'Toys', 4, TRUE);
INSERT INTO petwell_product (seller_id_id, name, price, quantity, animal, producttype, rating, approved) VALUES
(1, 'Dog Shampoo', 15, 50, 'Dog', 'Grooming', 5, TRUE),
(2, 'Cat Scratching Post', 30, 20, 'Cat', 'Furniture', 4, TRUE),
(3, 'Bird Cage', 45, 10, 'Bird', 'Housing', 5, TRUE),
(4, 'Rabbit Food', 10, 100, 'Rabbit', 'Food', 4, TRUE),
(5, 'Fish Tank Filter', 25, 30, 'Fish', 'Accessories', 4, TRUE),
(1, 'Dog Leash', 12, 60, 'Dog', 'Accessories', 5, TRUE),
(2, 'Cat Bed', 20, 25, 'Cat', 'Bedding', 4, TRUE),
(3, 'Parrot Toys', 18, 40, 'Bird', 'Toys', 4, TRUE),
(4, 'Hamster Wheel', 22, 35, 'Hamster', 'Exercise', 5, TRUE),
(5, 'Reptile Heat Lamp', 35, 15, 'Reptile', 'Heating', 4, TRUE);



INSERT INTO petwell_purchase (date, paid, delivery_status, product_id_id, customer_id_id) VALUES
('2025-03-20 10:00:00', TRUE, 'Delivered', 1, 1),
('2025-03-21 11:00:00', FALSE, 'Pending', 2, 1),
('2025-03-22 12:00:00', TRUE, 'Shipped', 3, 2),
('2025-03-23 13:00:00', TRUE, 'Delivered', 4, 2),
('2025-03-24 14:00:00', FALSE, 'Processing', 5, 3),
('2025-03-25 15:00:00', TRUE, 'Delivered', 6, 3),
('2025-03-26 16:00:00', FALSE, 'Pending', 7, 4);
INSERT INTO petwell_purchase (date, paid, delivery_status, product_id_id, customer_id_id) VALUES
('2025-03-10 10:00:00', TRUE, 'Delivered', 1, 1),
('2025-03-11 11:00:00', TRUE, 'Pending', 2, 1),
('2025-03-12 12:00:00', FALSE, 'Processing', 3, 2),
('2025-03-13 13:00:00', TRUE, 'Shipped', 4, 2),
('2025-03-14 14:00:00', FALSE, 'Pending', 5, 3),
('2025-03-15 15:00:00', TRUE, 'Delivered', 6, 3),
('2025-03-16 16:00:00', TRUE, 'Processing', 7, 4),
('2025-03-17 17:00:00', FALSE, 'Shipped', 8, 4),
('2025-03-18 18:00:00', TRUE, 'Delivered', 9, 5),
('2025-03-19 19:00:00', FALSE, 'Pending', 10, 5);