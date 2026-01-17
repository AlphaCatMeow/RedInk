<template>
  <div class="log-viewer card">
    <div class="section-header">
      <div>
        <h2 class="section-title">系统日志</h2>
        <p class="section-desc">实时查看后端运行日志</p>
      </div>
      <div class="actions">
        <label class="toggle-switch">
          <input type="checkbox" v-model="autoScroll">
          <span class="toggle-label">自动滚动</span>
        </label>
        <button class="btn btn-small btn-secondary" @click="clearLogs">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"></path>
          </svg>
          清空
        </button>
        <button class="btn btn-small" @click="toggleConnection">
          <span class="status-dot" :class="{ active: isConnected }"></span>
          {{ isConnected ? '已连接' : '已断开' }}
        </button>
      </div>
    </div>

    <div class="terminal-window" ref="terminalRef">
      <div v-if="logs.length === 0" class="empty-state">
        暂无日志数据...
      </div>
      <div v-else class="log-content">
        <div v-for="(log, index) in logs" :key="index" class="log-line">
          <span class="line-number">{{ index + 1 }}</span>
          <span class="line-text" :class="getLogClass(log)">{{ log }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'

const logs = ref<string[]>([])
const isConnected = ref(false)
const autoScroll = ref(true)
const terminalRef = ref<HTMLElement | null>(null)
let eventSource: EventSource | null = null

// 连接到日志流
const connect = () => {
  if (eventSource) return

  // 获取 API Base URL (根据环境)
  const baseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:12398'
  const url = `${baseUrl}/api/logs/stream`

  try {
    eventSource = new EventSource(url)
    
    eventSource.onopen = () => {
      isConnected.value = true
      // 添加连接成功提示
      logs.value.push(`[SYSTEM] Connected to log stream at ${new Date().toLocaleTimeString()}`)
    }

    eventSource.onmessage = (event) => {
      if (event.data) {
        logs.value.push(event.data)
        // 限制日志行数，避免内存溢出 (增加到 10000 行)
        if (logs.value.length > 10000) {
          logs.value = logs.value.slice(-10000)
        }
        
        if (autoScroll.value) {
          scrollToBottom()
        }
      }
    }

    eventSource.onerror = () => {
      isConnected.value = false
      if (eventSource?.readyState === EventSource.CLOSED) {
        logs.value.push('[SYSTEM] Connection closed')
      } else {
        // logs.value.push('[SYSTEM] Connection error, retrying...')
      }
    }
  } catch (e) {
    console.error('Failed to connect to log stream', e)
    logs.value.push(`[SYSTEM] Failed to connect: ${e}`)
  }
}

const disconnect = () => {
  if (eventSource) {
    eventSource.close()
    eventSource = null
    isConnected.value = false
    logs.value.push(`[SYSTEM] Disconnected at ${new Date().toLocaleTimeString()}`)
  }
}

const toggleConnection = () => {
  if (isConnected.value) {
    disconnect()
  } else {
    connect()
  }
}

const clearLogs = () => {
  logs.value = []
}

const scrollToBottom = () => {
  nextTick(() => {
    if (terminalRef.value) {
      terminalRef.value.scrollTop = terminalRef.value.scrollHeight
    }
  })
}

const getLogClass = (log: string) => {
  if (log.includes('ERROR') || log.includes('Exception') || log.includes('❌')) return 'log-error'
  if (log.includes('WARNING') || log.includes('⚠️')) return 'log-warning'
  if (log.includes('INFO') || log.includes('✅') || log.includes('🚀')) return 'log-info'
  if (log.includes('DEBUG')) return 'log-debug'
  return ''
}

onMounted(() => {
  connect()
})

onUnmounted(() => {
  disconnect()
})

// 监听自动滚动开关
watch(autoScroll, (newVal) => {
  if (newVal) {
    scrollToBottom()
  }
})
</script>

<style scoped>
.log-viewer {
  margin-top: 24px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #1a1a1a;
}

.section-desc {
  font-size: 14px;
  color: #666;
  margin: 0;
}

.actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.terminal-window {
  background-color: #1e1e1e;
  color: #d4d4d4;
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.5;
  height: 400px;
  overflow-y: auto;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid #333;
}

.log-line {
  display: flex;
  white-space: pre-wrap;
  word-break: break-all;
}

.line-number {
  color: #555;
  min-width: 40px;
  text-align: right;
  margin-right: 12px;
  user-select: none;
}

.line-text {
  flex: 1;
}

.empty-state {
  color: #666;
  text-align: center;
  padding-top: 160px;
}

/* Log Levels Colors */
.log-error {
  color: #f48771;
}

.log-warning {
  color: #cca700;
}

.log-info {
  color: #89d185;
}

.log-debug {
  color: #569cd6;
}

/* Toggle Switch */
.toggle-switch {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #666;
  cursor: pointer;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #ccc;
  display: inline-block;
}

.status-dot.active {
  background-color: #42b883;
  box-shadow: 0 0 4px #42b883;
}

.btn-secondary {
  background-color: #f5f5f5;
  color: #666;
  border: 1px solid #ddd;
}

.btn-secondary:hover {
  background-color: #eee;
}
</style>
