print("hello");
#string concatination

s = "hello";
t = "brother" ;

print(s , t);

print(type(s));

x = 10
print(id(x))

x = 20
print(id(x))

names = ["hello","aditya", "shyam", "rohan"];
print(names);
names.append("rohan")
print(names);

names.insert(2,"ram");
print(names);

names.remove("rohan");
print(names);

names.pop(-1)
print(names);

no = [1,2,"jello",'4.5',True];
print(no);

note = ("hello", "hjas",3,45.4);
print(note);


#tuples
student = ("Aditya",22,"MCA")
name, age, course = student

print(name)
print(age)

#set
set_example = {1,2,34,34,5,6,1};
print(set_example);

set_example.add("hello");
print(set_example);

set_example.remove(34);
print(set_example);

a = {1,2,4};
print(set_example | a);  #union
print(set_example & a);  #intersection

#dictionary
student = {
    "name":"Aditya",
    "age":22,
    "course":"MCA"
}

print(student)

print(student["name"])
student["age"] = 23
student["city"] = "patna"
print(student)

