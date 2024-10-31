function getHalfHourIndices(time, split, signal) {

    const timeSplit = split || ':'
    const timeChar = signal || ':'

    // 将时间段拆分为开始时间和结束时间
    const [startTime, endTime] = time.split(timeSplit);

    // 将时间字符串转换为小时和分钟
    const [startHour, startMinute] = (startTime ?? '')?.split(timeChar)?.map(Number);
    const [endHour, endMinute] = (endTime ?? '')?.split(timeChar)?.map(Number);

    // 计算开始时间和结束时间对应的半小时下标
    const startIndex = startHour * 2 + Math.floor(startMinute / 30);
    const endIndex = endHour * 2 + Math.floor(endMinute / 30);

    // 生成从开始下标到结束下标的数组
    const indices = [];
    for (let i = startIndex + 1; i <= endIndex; i++) {
        indices.push(i);
    }

    return indices;
}

// 示例用法
const timePeriod = "00:00-0:30";
const indices = getHalfHourIndices(timePeriod, '-', ':');
console.log(indices);