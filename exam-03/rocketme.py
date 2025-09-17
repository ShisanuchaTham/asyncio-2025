import time
import asyncio
import httpx

student_id = "6610301009"

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์

    """
    TODO:
    - ส่ง GET request ไปยัง rocketapp ที่ path /fire/{student_id}
    - อ่านค่า time_to_target จาก response
    - return dict ที่มี:
        {
            "name": name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    end_time = time.perf_counter() - t0

    return{
            "name": name,
            "start_time": start_time,
            "time_to_target": data["time_to_target"],
            "end_time": end_time
          }

    pass

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")  # แสดงตอนเริ่ม main

    # TODO: สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = [asyncio.create_task(fire_rocket(f"Rocket-{i+1}",t0)) for i in range(3)]

    # TODO: รอให้ทุก task เสร็จและเก็บผลลัพธ์ตามลำดับ task
    results = await asyncio.gather(*tasks)

    # TODO: แสดงผล start_time, time_to_target, end_time ของแต่ละ rocket ตามลำดับ task
    for r in results:
        print(f"{r['name']}|start_time:{r['start_time']:.2f}sec|time_to_target:{r['time_to_target']:.2f}sec|end_time:{r['end_time']:.2f}sec")
        pass  # แสดงผล rocket
    # TODO: แสดงเวลารวมทั้งหมดตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย
    t_total = 0  # คำนวณ max end_time
    for r in results:
        if r['end_time'] > t_total:
            t_total = r['end_time']
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")

asyncio.run(main())