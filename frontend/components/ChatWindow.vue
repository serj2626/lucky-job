<script setup lang="ts">
const { messages, sendMessage, isConnected } = useChat();
const message = ref("");

const handleSend = () => {
  if (message.value.trim()) {
    sendMessage(message.value, props.recipientId);
    message.value = "";
  }
};
</script>

<template>
  <div class="chat-container">
    <div class="status" :class="{ online: isConnected, offline: !isConnected }">
      {{ isConnected ? "Online" : "Offline" }}
    </div>

    <div class="messages">
      <div v-for="msg in messages" :key="msg.id" class="message">
        {{ msg.text }}
      </div>
    </div>

    <input
      v-model="message"
      @keyup.enter="handleSend"
      placeholder="Type a message..."
    />
    <button @click="handleSend">Send</button>
  </div>
</template>

<style scoped>
.chat-container {
  border: 1px solid #ddd;
  padding: 1rem;
  max-width: 500px;
}
.status {
  padding: 0.5rem;
  color: white;
  font-weight: bold;
}
.online {
  background: green;
}
.offline {
  background: red;
}
.messages {
  height: 300px;
  overflow-y: auto;
  margin: 1rem 0;
}
</style>
