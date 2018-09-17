package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

//Random generation of number of total students 15 - 300
func random1() int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn((300-15)+1) + 15
}

//second rando func for the establishement of time that each stud needs with the prof
func random2() int {
	return rand.Intn(5000)
}



var m map[string]int             //map for times to names
var totalStud int                //total number of students to process
var bench = make([]string, 0, 5) //create array that will hold the students...their seats.
var wg sync.WaitGroup            // sync wait group so the main function doesn't end before the go routines
var c = make(chan int)           // channel to communicate the current student total


func studentBench(c chan int) {
	totalStud = random1()
	fmt.Println("Total Number of Students is: ", totalStud)
	m = make(map[string]int)
	//easiest way was to have 300 names....many other ways to do this but not the purpose here
	names := []string{"bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika", "bob", "jeff", "sebastian", "lucita", "belle", "jasmine", "sasha", "olive", "avery", "opa",
		"oma", "hong", "kong", "delilah", "pikapika"}
	t := 0

	//change var to totalStud when done
	for t < totalStud {

		if len(bench) < 5 {
			index := t
			name := names[index]
			wait := random2()
			m[name] = int(wait)
			bench = append(bench, name)
			t++
		}
		//place channel input
		c <- t
	}
	close(c)
	wg.Done()

	//return bench
}

func prof(c chan int) {

	//needs to be totalStud
	//totalStudProf := <-d
	for i := range c {
		x := i
		fmt.Print(x)
		if x >= 5 {
			//only ever take m[0]
			fmt.Println(bench[0], " can now come in my office.")
			timeWait := m[bench[0]]
			fmt.Println("Spending time time with a student in Milliseconds:  ", timeWait)
			time.Sleep(time.Duration(timeWait) * time.Millisecond)
			//tell the student to leave
			fmt.Println(bench[0], " that was inspiring...you may leave now.")
			//remove student from map
			//delete from map
			delete(m, bench[0])
			//remove student zero from map and then from array
			i := 0
			bench = append(bench[:i], bench[i+1:]...)
			//time in office equals m["name"]
			fmt.Println("New Map: ", m)

		} else {
			fmt.Println("Playing halo while I wait for more students...")
		}
	}

	fmt.Println("Locking up and leaving for the day, no more kids left!")
	//start over
	wg.Done()
}

func main() {
	//all global varials defined above
	//Adds two threads or go routines to the wait list
	wg.Add(2)
	//starts studentBenchFunction
	go studentBench(c)
	go prof(c)
	wg.Wait()
}
