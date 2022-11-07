import redis from 'redis';
const client = redis.createClient();

client.on("error", (error) => {
	  if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
	  console.log('Redis client connected to the server');
});

const publishMessagw = (message, time) => {
	  setTimeout(() => {
		      console.log(`About to send ${messsage}`);
		      client.publish('holberton school channel', message);
		    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Studnet #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

